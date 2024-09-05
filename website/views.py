from datetime import datetime

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the meeting planner")


def date(request):
    return HttpResponse("This page was served at: " + str(datetime.now()))


def about(request):
    return HttpResponse("""
    <html>
        <body>
            <h1>About</h1>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac efficitur ante. Sed consequat 
                ullamcorper leo, ut vulputate turpis tristique ultrices. Ut tincidunt, justo eget pretium euismod, 
                odio quam congue arcu, a suscipit augue nisi sed massa. Praesent eleifend dapibus ultrices. Fusce 
                non sollicitudin nunc. Duis ultrices tellus sed diam volutpat semper. Donec dignissim purus eget 
                nulla elementum ullamcorper. Vivamus tincidunt vel massa vel fermentum. Quisque fringilla nisi orci, 
                ut congue leo lacinia eget. Sed lobortis enim est, a faucibus tellus rutrum et. Vestibulum a quam 
                euismod, vehicula dui in, placerat diam.
            </p>
        </body>
    </html>
    """)
