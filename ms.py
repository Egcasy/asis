from flask_sqlalchemy import SQLAlchemy<br>from flask_login import UserMixin<br><br>db = SQLAlchemy()<br><br>class User(UserMixin, <a href="http://db.Model">db.Model</a>):<br>&nbsp;&nbsp;&nbsp; __tablename__ = 'users'<br>&nbsp;&nbsp;&nbsp; id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, primary_key=True)<br>&nbsp;&nbsp;&nbsp; username = <a href="http://db.Column">db.Column</a>(<a href="http://db.String">db.String</a>(<a href="tel:150">150</a>), unique=True, nullable=False)<br>&nbsp;&nbsp;&nbsp; password = <a href="http://db.Column">db.Column</a>(<a href="http://db.String">db.String</a>(<a href="tel:150">150</a>), nullable=False)<br>&nbsp;&nbsp;&nbsp; friends = <a href="http://db.relationship">db.relationship</a>('FriendRequest', backref='user', lazy=True)<br><br>class FriendRequest(<a href="http://db.Model">db.Model</a>):<br>&nbsp;&nbsp;&nbsp; __tablename__ = 'friend_requests'<br>&nbsp;&nbsp;&nbsp; id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, primary_key=True)<br>&nbsp;&nbsp;&nbsp; sender_id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, <a href="http://db.ForeignKey">db.ForeignKey</a>('<a href="http://users.id">users.id</a>'), nullable=False)<br>&nbsp;&nbsp;&nbsp; receiver_id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, <a href="http://db.ForeignKey">db.ForeignKey</a>('<a href="http://users.id">users.id</a>'), nullable=False)<br>&nbsp;&nbsp;&nbsp; status = <a href="http://db.Column">db.Column</a>(<a href="http://db.String">db.String</a>(50), nullable=False)&nbsp; # "pending", "accepted", "rejected"<br><br>class Post(<a href="http://db.Model">db.Model</a>):<br>&nbsp;&nbsp;&nbsp; id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, primary_key=True)<br>&nbsp;&nbsp;&nbsp; content = <a href="http://db.Column">db.Column</a>(<a href="http://db.Text">db.Text</a>, nullable=False)<br>&nbsp;&nbsp;&nbsp; user_id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, <a href="http://db.ForeignKey">db.ForeignKey</a>('<a href="http://users.id">users.id</a>'), nullable=False)<br><br>class Comment(<a href="http://db.Model">db.Model</a>):<br>&nbsp;&nbsp;&nbsp; id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, primary_key=True)<br>&nbsp;&nbsp;&nbsp; content = <a href="http://db.Column">db.Column</a>(<a href="http://db.Text">db.Text</a>, nullable=False)<br>&nbsp;&nbsp;&nbsp; post_id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, <a href="http://db.ForeignKey">db.ForeignKey</a>('<a href="http://post.id">post.id</a>'), nullable=False)<br>&nbsp;&nbsp;&nbsp; user_id = <a href="http://db.Column">db.Column</a>(<a href="http://db.Integer">db.Integer</a>, <a href="http://db.ForeignKey">db.ForeignKey</a>('<a href="http://users.id">users.id</a>'), nullable=False)