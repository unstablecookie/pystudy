from sqlalchemy import (
	Table , Text , Integer, VARCHAR,MetaData,Column
	)

meta = MetaData()
kek1 = Table(
	'kek',meta,
	Column('id',integer, primary_key=True),
	Column('title',VARCHAR,nullable=True),
	Column('body', Text)
	)