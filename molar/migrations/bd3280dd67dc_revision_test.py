"""revision_test

Revision ID: bd3280dd67dc
Revises: f31c7d486f1f
Create Date: 2021-10-24 00:23:08.010496

"""
from alembic import op
from sqlalchemy.dialects import postgresql as pgsql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd3280dd67dc'
down_revision = 'f31c7d486f1f'
branch_labels = ('stober_db_creation',)
depends_on = None


def upgrade():
    op.create_table(
        "Operator",
        sa.Column("id_operator", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("mail", sa.String(50), nullable=False),
        schema="public",
    )
    op.create_table(
        "Compound",
        sa.Column("id_compound", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("CAS", sa.String(50), nullable=True),
        sa.Column("name", sa.String(50), nullable=True),
        sa.Column("purity", sa.Float, nullable=True),
        schema="public",
    )
    op.create_table(
        "Characterization",
        sa.Column("id_characterization", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("technique", sa.String(50), nullable=True),
        sa.Column("value", sa.Float, nullable=True),
        sa.Column("standard_deviation", sa.Float, nullable=True),
        schema="public",
    )
    op.create_table(
        "Data_source",
        sa.Column("id_data_source", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("secondary_data", sa.Boolean, nullable=True),
        sa.Column("year", sa.Integer, nullable=True),
        sa.Column("reference", sa.String(50), nullable=True),
        schema="public",
    )
    op.create_table(
        "Reagent",
        sa.Column("id_characterization", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("technique", sa.String(50), nullable=True),
        sa.Column("value", sa.Float, nullable=True),
        sa.Column("standard_deviation", sa.Float, nullable=True),
        sa.Column('id_compound', pgsql.UUID, sa.ForeignKey('Compound.id_compound')),
        schema="public",
    )
    op.create_table(
        "Synthesis",
        sa.Column("id_synthesis", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column("agitation_speed", sa.String(50), nullable=True),
        sa.Column("temperature", sa.Float, nullable=True),
        sa.Column("residence_time", sa.Float, nullable=True),
        sa.Column("volume_reactor", sa.Float, nullable=True),
        sa.Column('id_data_source', pgsql.UUID, sa.ForeignKey('Data_source.id_data_source')),
        schema="public",
    )
    op.create_table(
        "Experiment",
        sa.Column("id_experiment", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column('id_synthesis', pgsql.UUID, sa.ForeignKey('Synthesis.id_synthesis')),
        sa.Column('id_operator', pgsql.UUID, sa.ForeignKey('Operator.id_operator')),
        sa.Column("date", sa.Date, nullable=True),
        schema="public",
    )
    op.create_table(
        "Synthesis_Compound",
        sa.Column("id_synthesis_compound", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column('id_synthesis', pgsql.UUID, sa.ForeignKey('Synthesis.id_synthesis')),
        sa.Column('id_compound', pgsql.UUID, sa.ForeignKey('Compound.id_compound')),
        sa.Column("concentration", sa.Float, nullable=True),
        schema="public",
    )
    op.create_table(
        "Product_Characterization",
        sa.Column("id_product_characterization", pgsql.UUID, primary_key=True, nullable=False),
        sa.Column('id_synthesis', pgsql.UUID, sa.ForeignKey('Synthesis.id_synthesis')),
        sa.Column('id_characterization', pgsql.UUID, sa.ForeignKey('Characterization.id_characterization')),
        schema="public",
    )

def downgrade():
    # TODO: complete dropping columns in the reverse order as they were created
    pass
