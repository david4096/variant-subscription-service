from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import *

CHROMOSOMES = [str(x) for x in range(1, 23)]
CHROMOSOMES.extend(['X', 'Y', 'MT', 'M'])
CHROMOSOMES.extend(['chr{}'.format(x) for x in CHROMOSOMES])


class SignupForm(FlaskForm):
    # email = StringField(u'Your email address', validators=[Email(), DataRequired()])
    # chromosome = StringField(u'Chromosome', validators=[DataRequired(), AnyOf(CHROMOSOMES)])
    # position = IntegerField(u'Position', validators=[DataRequired()])
    # reference = StringField(u'Reference allele', validators=[DataRequired()])
    # alternate = StringField(u'Alternate allele', validators=[DataRequired()])

    eula = BooleanField(u'I did not read the terms and conditions')

    submit = SubmitField(u'Signup')
