import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
sys.path.append(os.getcwd)


engine = create_engine('sqlite:///db/restaurants.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)
    concerts = relationship('Restaurant', back_populates='band')

    def customers(self):
        return self.concerts

    def reviews(self):
        return [concert.venue for concert in self.concerts]

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        session.add(concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count().desc()).first()


    def __repr__(self):
	@@ -29,11 +44,54 @@ def __repr__(self):

class Review(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    concerts = relationship('Restaurant', back_populates='review')

    def Restaurant(self):
        return self.restaurant

    def customers(self):
        return [restaurant.customers for restaurant in self.concerts]

    def retaurant_on(self, date):
        return session.query(Restaurant).filter_by(date=date, venue=self).first()

    def most_frequent_customer(self):
        customer_counts = {}
        for restaurants in self.restaurants:
            customer = restaurants.customers
            if customer in customer_counts:
                customer_counts[customer] += 1
            else:
                customer_counts[customer] = 1
        return max(customer_counts, key=customer_counts.get)

    def __repr__(self):
        return f'Review: {self.title}'

class Restaurant(Base):
    __tablename__ = 'retaurants'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    name = Column(String)
    band_id = Column(Integer, ForeignKey('customer.id'))
    venue_id = Column(Integer, ForeignKey('review.id'))
    band = relationship('Cutsomer', back_populates='restaurants')
    review = relationship('Review', back_populates='restaurants')

    def band(self):
        return self.customer

    def Review(self):
        return self.review

    def Restaurant_fanciest(self):
        return self.restaurant
    def full_review(self):
        return  {self.review.restaurant}
    def __repr__(self):
        return f'Restaurant {self.name}'