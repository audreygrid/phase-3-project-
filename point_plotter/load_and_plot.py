from models import init_db, get_session, PointClass
from point_plotter import create_canvas, clear_screen, render_canvas, plot_point, WIDTH, HEIGHT

engine = init_db()
session = get_session(engine)

# Load shape by name
shape = session.query(PointClass).filter_by(name="Triangle").first()

canvas = create_canvas(WIDTH, HEIGHT)

# Plot it
if shape:
    for point in shape.points:
        plot_point(canvas, point.x, point.y, '*')

    clear_screen()
    print(f"{shape.name} - {shape.description}")
    render_canvas(canvas)
else:
    print("Shape not found.")