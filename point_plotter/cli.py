from models import init_db, get_session, PointClass, Point
from point_plotter import create_canvas, clear_screen, render_canvas, plot_point, draw_line, WIDTH, HEIGHT

engine = init_db()
session = get_session(engine)

def list_shapes():
    shapes = session.query(PointClass).all()
    if not shapes:
        print("No shapes found.")
    else:
        for shape in shapes:
            print(f"[{shape.id}] {shape.name} - {shape.description}")

def view_shape():
    try:
        shape_id_str = input("Enter shape ID to view: ")
        shape_id = int(shape_id_str)
    except ValueError:
        print(f"Invalid input: '{shape_id_str}' is not a valid number. Please enter a numeric ID.")
        return

    shape = session.query(PointClass).get(shape_id)

    if not shape:
        print(f"Shape with ID {shape_id} not found.")
        return

    canvas = create_canvas(WIDTH, HEIGHT)
    if shape.points:
        # Plot first point
        plot_point(canvas, shape.points[0].x, shape.points[0].y)
        # Draw lines between subsequent points
        for i in range(len(shape.points) - 1):
            p1 = shape.points[i]
            p2 = shape.points[i+1]
            draw_line(canvas, p1.x, p1.y, p2.x, p2.y)
        # Optionally, draw a line from the last point to the first to close the shape
        # if len(shape.points) > 2: # Only close if it's a polygon
        #     p_last = shape.points[-1]
        #     p_first = shape.points[0]
        #     draw_line(canvas, p_last.x, p_last.y, p_first.x, p_first.y)


    clear_screen()
    print(f"{shape.name} - {shape.description}")
    render_canvas(canvas)

def create_shape():
    name = input("Enter shape name: ")
    description = input("Enter description: ")

    shape = PointClass(name=name, description=description)

    print("Enter points one at a time as 'x y'. Type 'done' to finish.")
    while True:
        raw = input("Point: ")
        if raw.lower() == 'done':
            break
        try:
            x_str, y_str = raw.strip().split()
            x, y = int(x_str), int(y_str)
            shape.points.append(Point(x=x, y=y))
        except ValueError:
            print("Invalid format. Please enter as 'x y'.")

    session.add(shape)
    session.commit()
    print(f"Shape '{name}' saved!")

def delete_shape():
    try:
        shape_id_str = input("Enter shape ID to delete: ")
        shape_id = int(shape_id_str)
    except ValueError:
        print(f"Invalid input: '{shape_id_str}' is not a valid number. Please enter a numeric ID.")
        return
    shape = session.query(PointClass).get(shape_id)
    if shape:
        session.delete(shape)
        session.commit()
        print("Shape deleted.")
    else:
        print(f"Shape with ID {shape_id} not found.")

def main_menu():
    while True:
        print("\n--- Point Plotter CLI ---")
        print("1. List shapes")
        print("2. View a shape")
        print("3. Create a new shape")
        print("4. Delete a shape")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_shapes()
        elif choice == '2':
            view_shape()
        elif choice == '3':
            create_shape()
        elif choice == '4':
            delete_shape()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()