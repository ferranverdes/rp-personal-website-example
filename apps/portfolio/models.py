from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField()
	preview_image = models.FilePathField(path="/img")
	reference_link = models.URLField(max_length=250)

	def __str__(self):
		return self.title

# CharField is used for short strings and specifies a maximum length.
# TextField is similar to CharField but can be used for longer form text as it
# doesn’t have a maximum length limit.
# FilePathField also holds a string but must point to a file path name.
# URLField is a CharField for an URL, validated by URLValidator.

# __str__ function returns the representation, as string, for every Project instance.
