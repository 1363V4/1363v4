from flask import render_template, request, session
from jinja2_fragments.flask import render_block
import networkx as nx
from pruned_aliases import pruned_aliases
from flags import flags


KEYS = "c/g/d/a/e/b/f#/c#/g#/d#/a#/f".split("/")
LEN_KEYS = len(KEYS)
MODES = "lydien/majeur/mixo/dorien/minor/phrygien/locrien".split("/")
LEN_MODES = len(MODES)


def is_htmx():
    return 'hx-request' in request.headers

def hx_boost_content(route, *args, **kwargs):
    if is_htmx():
        return render_block(route, "content", *args, **kwargs)
    else:
        return render_template(route, *args, **kwargs)

def get_answer(G, start, end):        
    try:
        short = nx.shortest_path(G, start, end, weight=1)
    except:
        short = []
    match len_short := len(short):
        case 0:
            good_button = "impossible"
        case len_short if len_short < 8:
            good_button = "6 ou -"
        case _:
            good_button = "7 ou +"
    return good_button, short

def alias(id):
    alias = pruned_aliases[id]
    city, country = alias.split("___")
    if code := flags.get(country):
        return f'{city} <img class="flag_img" src="/static/img/flags/{code}.png">'
    else:    
        return f"{city} (in {country})"
    
def alias_gmap(id):
    alias = pruned_aliases[id]
    city, country = alias.split("___")
    msg = f"{city}+{country}"
    msg = "+".join([word for word in msg.split()])
    return msg

def gmap(path):
    api_key = "AIzaSyCdxnjBphEaFER2rhGLQTUX8-zDvYWYFOo"
    params = f"origin={path.pop(0)}"
    params += f"&destination={path.pop()}"
    waypoints = '|'.join(city for city in path)
    params += f"&waypoints={waypoints}"
    new_div = f'''
    <form
    hx-post="/jumelio"
    hx-target="main">
        <button id="b1" type="submit" name="button" value="back">back</button>
    </form>
    <iframe
    frameborder="0"
    referrerpolicy="no-referrer-when-downgrade"
    src="https://www.google.com/maps/embed/v1/directions?key={api_key}&{params}"
    allowfullscreen>
    </iframe>'''
    return new_div

def render_circle():
    value = session['circle']
    name = KEYS[session['key']]
    name += " "
    name += MODES[session['mode']]
    new_div = f'''
    <h1 id="scale" hx-swap-oob="true">{name}</h1>
    <div id="circle" class="circle" style="transform: rotate({value}deg)">
      <img src="/static/img/circle/full_circle.svg">
    </div>
    '''
    return new_div

def render_half_circle():
    value = session['half_circle']
    brightness = 1.6 + (value - 30) / 180
    brightness = round(brightness, 2)
    name = KEYS[session['key']]
    name += " "
    name += MODES[session['mode']]
    new_div = f'''
    <h1 id="scale" hx-swap-oob="true">{name}</h1>
    <div id="half_circle" class="half_circle" style="transform: rotate({value}deg); filter: brightness({brightness})">
      <img src="/static/img/circle/half_circle.svg">
    </div>
    '''
    return new_div
