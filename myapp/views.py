from django.shortcuts import render, get_object_or_404
from .models import Person


def index(request):
	
	if Person.objects.count() == 0:
		Person.objects.create(  
			name='Ralph Ivan Censon',
			title='Frontend Developer',
			bio=' Creating interactable website using figma designs.',
			about='Im Ralph ivan Censon. My hobbies are playing badminton, designing websites/making website using figma. Currently Studying at Sta maria sti college, my goal is to become good at coding.',
			email='ralphivan2005@gmail.com',
			website='https://example.com/Censon'
		)
		Person.objects.create(
			name='Johann Marqueta',
			title='Backend Engineer',
			bio='Develops Games and other apps.',
			about='IT enthusiast passionate about game development. With a background in IT tech, focusing on making backend systems efficient and reliable. Experienced with cloud infrastructure and databases.',
			email='marqjohannmarqueta@gmail.com',
			website='https://example.com/Marqueta'
		)

	people = Person.objects.all()
	return render(request, 'myapp/index.html', {'people': people})


def detail(request, pk):
	person = get_object_or_404(Person, pk=pk)
	return render(request, 'myapp/detail.html', {'person': person})
