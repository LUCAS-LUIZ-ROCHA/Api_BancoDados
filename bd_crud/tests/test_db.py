from sqlalchemy import select

from bd_crud.models import User


def test_create_user(session):
    new_user = User(
        username='Lucas Luiz', password='secret123', email='lucas@example.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.usermane == 'Lucas Luiz'))

    assert user.username == 'Lucas Luiz'
