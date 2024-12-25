from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Workout_Model(Base):
    __tablename__ = "workouts"
    id: Mapped[int] = mapped_column(autoincrement=True,primary_key=True, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False)
    exercises: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    split: Mapped[str] = mapped_column(nullable=False)
    reps: Mapped[str] = mapped_column(nullable=False)
    sets: Mapped[str] = mapped_column(nullable=False)
    rest_time: Mapped[int] = mapped_column(nullable=False)
    day: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)

class Exercise_Model(Base):
    __tablename__ = "exercises"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    technique: Mapped[str] = mapped_column(nullable=False)

class User_Model(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    workouts: Mapped[str] = mapped_column(nullable=False)
    awards: Mapped[str] = mapped_column(nullable=False)

class Rating_Model(Base):
    __tablename__ = "ratings"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    level: Mapped[int] = mapped_column(nullable=False)
    requirements: Mapped[str] = mapped_column(nullable=False)
    exercise: Mapped[str] = mapped_column(nullable=False)
    details: Mapped[str] = mapped_column(nullable=False)

class Progress_Model(Base):
    __tablename__ = "progress"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False)
    user: Mapped[int] = mapped_column(nullable=False)
    workouts: Mapped[str] = mapped_column(nullable=False)

class Achievements_Model(Base):
    __tablename__ = "achievements"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    slug: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    details: Mapped[str] = mapped_column(nullable=False)
    requirments: Mapped[str] = mapped_column(nullable=False)
