from models import init_db, get_session, PointClass, Point

engine = init_db()
session = get_session(engine)

# Create a new shape
shape = PointClass(name="Triangle", description="A simple triangle")
shape.points = [
    Point(x=5, y=5),
    Point(x=6, y=6),
    Point(x=7, y=5)
]

session.add(shape)
session.commit()
print("Shape saved!")