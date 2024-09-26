from flask import Flask, redirect, render_template, request, session, url_for
from jinja2_fragments.flask import render_block
from utils import hx_boost_content, get_answer, alias, alias_gmap, gmap, render_circle, render_half_circle, LEN_KEYS, LEN_MODES
import secrets
import uuid
from random import choice
import networkx as nx
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import time
import chess
import htmlgenerator as hg
from h import h_chessboard, make_steps
from turten import d_turten


devdir = Path(__file__).parent
G = nx.read_adjlist(devdir / "pruned_network.adjlist")
nodes = list(G.nodes)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return hx_boost_content("index.html")
    elif request.method == "POST":
        match request.values.get('button'):
            case "jumelio":
                return redirect(url_for('jumelio'))
            case "echecs":
                return redirect(url_for('echecs'))
            case "triangle":
                return redirect(url_for('triangle'))
            case "circle":
                return redirect(url_for('circle'))
            case "story":
                return redirect(url_for('story'))
            case "turten":
                return redirect(url_for('turten'))
            case "css":
                return redirect(url_for('css'))
            case _:
                print("fuck")


@app.route('/echecs', methods=['GET', 'POST'])
def echecs():
    if request.method == "GET":
        session['fen'] = chess.STARTING_BOARD_FEN
        session['to_squares'] = []
        return h_chessboard(session['fen'])
    elif request.method == "POST":
        outcome = None
        board = chess.Board(session['fen'])
        clicked_square = int(request.headers['Hx-Trigger'])
        piece = board.piece_at(clicked_square)
        if piece and piece.color == chess.WHITE:
            session['from_square'] = clicked_square
            session['to_squares'] = []
            legal_moves = list(board.legal_moves)
            for move in legal_moves:
                if move.from_square == clicked_square:
                    session['to_squares'] += [move.to_square]
        elif clicked_square in session['to_squares']:
            session['to_squares'].clear()
            move = chess.Move(from_square=session['from_square'], to_square=clicked_square)
            board.push(move)
            if board.outcome():
                outcome = board.outcome()
            else:
                legal_moves = list(board.legal_moves)
                move = choice(legal_moves)
                board.push(move)
            if board.outcome():
                outcome = board.outcome()
            session['fen'] = board.fen()
        else:
            session['to_squares'].clear()
        return h_chessboard(
            session['fen'],
            context={
                'from_square': clicked_square,
                'to_squares': session['to_squares'],
                'outcome': outcome
            }
        )


@app.route('/jumelio', methods=['GET', 'POST'])
def jumelio():
    if request.method == "GET":
        session['tries'] = 0
        session['score'] = 0
        return hx_boost_content('jumelio.html')
    elif request.method == "POST":
        if session['tries'] > 4 and request.values.get('button') == "next":
            return hx_boost_content(
                'jumelio_end.html',
                score=session['score']
                )
        match request.values.get('button'):
            case "start":
                session['start'] = "2609"#choice(nodes)
                session['end'] = "8225"#choice(nodes)
                return hx_boost_content(
                    'jumelio_game.html',
                    start=alias(session['start']),
                    end=alias(session['end'])
                    )
            case "impossible" | "6 ou -" | "7 ou +":
                session['result'] = "LOSE"
                session['tries'] += 1 
                session['good_button'], session['answer'] = get_answer(G, session['start'], session['end'])
                if request.values['button'] == session['good_button']:
                    print("trop fort")
                    session['result'] = "WIN"
                    session['score'] += 1
                result_format = "result_win" if session['result'] == "WIN" else "result_lose"
                return hx_boost_content(
                    'jumelio_answer.html',
                    result=f"<div class='{result_format}'>{session['result']}</div>",
                    answer="<p> -> ".join([alias(city) for city in session['answer']]) if session['answer'] else "<p>pas possible<p>",
                    score=session['score'],
                    map=True if session['answer'] else False
                    )
            case "map":
                return gmap([alias_gmap(city) for city in session['answer']])
            case "back":
                result_format = "result_win" if session['result'] == "WIN" else "result_lose"
                return hx_boost_content(
                    'jumelio_answer.html',
                    result=f"<div class='{result_format}'>{session['result']}</div>",
                    answer="<p> -> ".join([alias(city) for city in session['answer']]) if session['answer'] else "<p>pas possible<p>",
                    score=session['score'],
                    map=True if session['answer'] else False
                    )
            case "next":
                session['start'] = choice(nodes)
                session['end'] = choice(nodes)
                return hx_boost_content(
                    'jumelio_game.html',
                    start=alias(session['start']),
                    end=alias(session['end'])
                    )
            case _:
                print("fuck")


@app.route('/triangle', methods=['GET', 'POST'])
def triangle():
    if request.method == "GET":
        return hx_boost_content('triangle.html')
    elif request.method == "POST":
        triangle_id = uuid.uuid4()
        base_length = 10
        #base_length = request.values.get('physique')
        #angle1 = request.values.get('affectif')
        #angle2 = request.values.get('intellectuel')
        #height = int(base_length) * np.tan(np.radians(int(angle1)))
        points = [(0, 0), (base_length, 0), (base_length, 1), (0, 0)]

        plt.plot(*zip(*points))
        plt.axis('off')
        plt.savefig(devdir / "static" / "img" / "tmp" / f"t_{triangle_id}.png", transparent=True)
        time.sleep(3)
        
        return hx_boost_content(
            'triangle_answer.html',
            stuff=triangle_id)


@app.route('/circle')
def circle():
    session['key'] = 0
    session['mode'] = 1
    session['circle'] = 0
    session['half_circle'] = 0
    return hx_boost_content("circle.html")


@app.route('/rotate_plus')
def rotate_plus():
    session['key'] -= 1
    session['key'] %= LEN_KEYS
    session['circle'] += 30
    return render_circle()


@app.route('/rotate_minus')
def rotate_minus():
    session['key'] += 1
    session['key'] %= LEN_KEYS
    session['circle'] -= 30
    return render_circle()


@app.route('/rotate_half_plus')
def rotate_half_plus():
    if session['mode'] > 0:
        session['mode'] -= 1
        session['mode'] %= LEN_MODES
        session['half_circle'] += 30
    return render_half_circle()


@app.route('/rotate_half_minus')
def rotate_half_minus():
    if session['mode'] < 6:
        session['mode'] += 1
        session['mode'] %= LEN_MODES
        session['half_circle'] -= 30
    return render_half_circle()


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/story')
def story():
    steps = make_steps()
    return hx_boost_content("story.html", steps=steps)


@app.route('/turten')
def turten():
    return hx_boost_content("turten.html")


@app.route('/decode', methods=['POST'])
def decode():
    out = []
    txt = request.values.get('decode')
    for num in txt.split("."):
        out += [d_turten.get(num, num)]
    return "".join(out)


@app.route('/encode', methods=['POST'])
def encode():
    txt = request.values.get('encode').lower()
    point = request.values.get('point') == "on"
    out = []
    for char in txt:
        out += [d_turten.get(char, char)]
    return ".".join(out) if point else "".join(out)


@app.route('/css')
def css():
    return hx_boost_content("css.html")


@app.route('/css_calc')
def css_calc():
    var_0 = request.values.get('var_0')
    var_1 = request.values.get('var_1')
    var_2 = request.values.get('var_2')
    txt = f"var(--{var_1}) * var(--{var_2}) + calc(var(--{var_0}) * (1 - var(--{var_2})))"
    return txt


if __name__ == '__main__':
    app.run(debug=True)
