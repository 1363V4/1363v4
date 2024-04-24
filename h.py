import chess
import htmlgenerator as hg
from random import choice


def h_chessboard(fen, context=None):
    board = chess.Board(fen)
    content = hg.BaseElement()
    content += [hg.DIV(
        _class="board"
        )]
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        img_id = str(piece).lower() + "dl"[piece.color] if piece else None
        img = f"<img class='chess_img' src='/static/img/chess/pieces/{img_id}.svg'>" if img_id else None
        if img:
            content[0] += [
                hg.DIV(
                    hg.mark_safe(img),
                    id=f"{square}",
                    _class=["square black", "square white"][(square // 8 + square) % 2],
                    **{
                        'hx-post': "/echecs",
                        'hx-target': "main"
                        }
                    )
                    ]
        else:
            content[0] += [
                hg.DIV(
                    id=f"{square}",
                    _class=["square black", "square white"][(square // 8 + square) % 2],
                    **{
                        'hx-post': "/echecs",
                        'hx-target': "main"
                        }
                    )
                    ]
    if context:
        from_square = context['from_square']
        content[0][from_square].attributes['_class'] = "square selected"
        to_squares = context['to_squares']
        for to_square in to_squares:
            content[0][to_square].attributes['_class'] = "square possible"
        if context.get('outcome'):
            print(context['outcome'])
            result = "win" if context['outcome'].winner == chess.WHITE else "lose"
            for square in chess.SQUARES:
                content[0][square].attributes['_class'] = f"square {result}"
            content += [
                hg.BUTTON("play again",
                **{
                    'hx-get': "/echecs",
                    'hx-target': "main",
                }
                )
                ]
    return hg.render(content, {})


def make_steps():
    steps = []
    for n in range(1, 8):
        step = hg.DIV()
        step += [n]
        way = choice(["up", "down"])
        step += [hg.IMG(_class="arrow",
            **{
            'src': f"/static/img/story/arrow-right-{way}-line.svg",
            })]
        step += [n+1]
        steps += [hg.render(step, {})]
    return steps