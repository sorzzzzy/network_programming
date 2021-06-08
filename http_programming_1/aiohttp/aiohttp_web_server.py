from aiohttp import web
import aiofiles

async def send_html(request):
    # async with aiofiles.open('index_button.html', 'r') as f: 
    # async with aiofiles.open('index_get.html', 'r') as f:
    async with aiofiles.open('index_post.html', 'r') as f:
        msg = await f.read()
        return web.Response(text=msg, content_type='text/html')


async def proc_query(request):
    print(request.query_string)
    parsed_query = request.query_string.split("=")
    status = parsed_query[1]

    if status == 'on':
        message = '<h2>LED in IoT Device is now turned on </h2>'
    elif status == 'off':
        message = '<h2>LED in IoT Device is now turned off </h2>'
    else:
        message = '<h2>Wrong Status</h2>'

    return web.Response(text=message, content_type='text/html')

async def proc_form_post(request):
    data = await request.post()
    print(data)
    status = data['status']
    if status == 'on':
        message = '<h2>LED in IoT Device is now turned on </h2>'
    elif status == 'off':
        message = '<h2>LED in IoT Device is now turned off </h2>'
    else:
        message = '<h2>Wrong Status</h2>'

    return web.Response(text=message, content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', send_html),
                web.get('/button', proc_query),
                web.get('/form_get', proc_query),
                web.post('/form_post', proc_form_post)])
web.run_app(app, port=8000)