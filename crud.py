from model import db, User, Event, connect_to_db


def create_user(email):
    """Create and return a new user."""

    user = User(email=email)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_movie(event_name, event_date):
    """Create and return a new event."""

    event = Event(
        event_name=event_name,
        event_date=event_date,

    )

    return event


def get_movies():
    """Return all events."""

    return Event.query.all()


def get_movie_by_id(event_id):
    """Return a event by primary key."""

    return Event.query.get(event_id)


def create_booking(user, event):
    """Create and return a new booking."""

    rating = Event(user=user, event=event)

    return rating


if __name__ == "__main__":
    from server import app

    connect_to_db(app)