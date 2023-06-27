import os
from QuerySystem import BookQuery
from constants import *

bookQuery = BookQuery(OPEN_AI_KEY, PINECONE_API_KEY, ENVIRONMENT_KEY)

bookQuery.loadThePDFS("https://firebasestorage.googleapis.com/v0/b/bookquerying.appspot.com/o/Q%20learning.pdf?alt=media&token=d4a6bbe9-3858-48ce-88bb-819419834e6f")