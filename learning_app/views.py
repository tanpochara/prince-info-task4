from django.shortcuts import render
from .models import Topic
from django.template import loader

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_app/index.html') 

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_app/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_app/topic.html', context)