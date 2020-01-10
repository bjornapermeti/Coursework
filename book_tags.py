from app.config import db


class BookTags(db.Model):
    __tablename__ = "book_tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    goodreads_book_id = db.Column(db.Integer)
    tag_id = db.Column(db.Integer)
    tag_name = db.Column(db.String(120))
    count = db.Column(db.Integer)

    @classmethod
    def get_tags(cls, gid, n=5):
        """Gets list of tags for a given book.

        Args:
            gid ([string]): Goodreads book id provided in the dataset.
                            Encountered as `goodreads_book_id`

        Returns:
            [List]: List of tag objects, each of which has a two fields (tag_id, count)
        """
        return [
            x.__dict__
            for x in (
                cls.query.filter_by(goodreads_book_id=gid)
                .order_by(cls.count.desc())
                .limit(n)
            )
        ]
