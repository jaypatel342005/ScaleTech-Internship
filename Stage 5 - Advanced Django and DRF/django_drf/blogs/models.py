from django.db import models

topics = [
    ('Technology', 'Technology'),
    ('Sports', 'Sports'),
    ('Entertainment', 'Entertainment'),
    ('Business', 'Business'),
    ('Health', 'Health'),
    ('Education', 'Education'),
    ('Travel', 'Travel'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion'),
    ('Politics', 'Politics'),
    ('Science', 'Science'),
    ('Art', 'Art'),
    ('Music', 'Music'),
    ('Photography', 'Photography'),
    ('Literature', 'Literature'),
    ('History', 'History'),
    ('Geography', 'Geography'),
    ('Mathematics', 'Mathematics'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('Astronomy', 'Astronomy'),
    ('Geology', 'Geology'),
    ('Meteorology', 'Meteorology'),
    ('Oceanography', 'Oceanography'),
    ('Computer Science', 'Computer Science'),
    ('Data Science', 'Data Science'),
    ('Artificial Intelligence', 'Artificial Intelligence'),
    ('Machine Learning', 'Machine Learning'),
    ('Deep Learning', 'Deep Learning'),
    ('Natural Language Processing', 'Natural Language Processing'),
    ('Computer Vision', 'Computer Vision'),
    ('Robotics', 'Robotics'),
    ('Internet of Things', 'Internet of Things'),
    ('Blockchain', 'Blockchain'),
    ('Cybersecurity', 'Cybersecurity'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Big Data', 'Big Data'),
    ('Web Development', 'Web Development'),
    ('Mobile Development', 'Mobile Development'),
    ('Game Development', 'Game Development'),
    ('Software Engineering', 'Software Engineering'),
    ('Database Management', 'Database Management'),
    ('Network Security', 'Network Security'),
    ('System Administration', 'System Administration'),
    ('DevOps', 'DevOps'),
    ('Agile Methodologies', 'Agile Methodologies'),
    ('Scrum', 'Scrum'),
    ('Kanban', 'Kanban'),
    ('Lean Methodologies', 'Lean Methodologies'),
    ('Six Sigma', 'Six Sigma'),
    ('Kaizen', 'Kaizen'),
    ('Just In Time', 'Just In Time'),
    ('Lean Manufacturing', 'Lean Manufacturing'),
    ('Total Quality Management', 'Total Quality Management'),
    ('Quality Assurance', 'Quality Assurance'),
    ('Quality Control', 'Quality Control'),
    ('Risk Management', 'Risk Management'),
    ('Change Management', 'Change Management'),
    ('Project Management', 'Project Management'),
    ('Program Management', 'Program Management'),
    ('Portfolio Management', 'Portfolio Management'),
    ('Strategic Management', 'Strategic Management'),
    ('Business Analysis', 'Business Analysis'),
    ('Data Analysis', 'Data Analysis'),
    ('Business Intelligence', 'Business Intelligence'),
    ('Data Mining', 'Data Mining'),
    ('Data Visualization', 'Data Visualization'),
    ('Data Engineering', 'Data Engineering'),
    ('Data Architecture', 'Data Architecture'),
    ('Data Governance', 'Data Governance'),
    ('Data Quality', 'Data Quality'),
    ('Data Security', 'Data Security'),
    ('Data Privacy', 'Data Privacy'),
    ('Data Protection', 'Data Protection'),
    ('Data Management', 'Data Management'),
    ('Data Strategy', 'Data Strategy'),
    ('Data Operations', 'Data Operations'),
    ('Data Analytics', 'Data Analytics'),
    ('Data Science', 'Data Science'),
]

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    topic = models.CharField(max_length=100,choices=topics)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE , related_name='comments')
    comment = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
