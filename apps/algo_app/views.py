# views.py is the Controller of the MVC architecture
# Note: controller and model methods were written to handle CRUD operations for all tables; this functionality has been replaced with Django admin and is therefore commented out (look at how much code Django admin saves!)

from django.shortcuts import render, HttpResponse, redirect
from .models import Algorithm, Tag, Language, Solution #, User
from django.core.urlresolvers import reverse
from django.contrib import messages

def index(request):

    # reset the 'show_solution' boolean to false
    request.session['show_solution'] = False

    # # if an admin boolean doesn't exist in session (i.e. fresh visit to page), create one and set to false as default
    # if 'admin_mode' not in request.session:
    #     new_admin = User.objects.create_admin()
    #     request.session['admin_mode'] = False

    # get all the tags, languages, and algorithms to populate the search and list areas of the index template
    tags = Tag.objects.get_all()
    languages = Language.objects.get_all()
    algorithms = Algorithm.objects.get_all()

    # put the information into an object to be rendered on the template
    context = {
        'tags': tags,
        'languages': languages,
        'algorithms': algorithms,
    }

    # render the template and pass the object containing the needed information
    return render(request, 'algo_app/index.html', context)

# def admin_login(request):
#     results = User.objects.login(request)
#     if results:
#         request.session['admin_mode'] = True
#     return redirect ('/')

# def admin_logout(request):
#     request.session['admin_mode'] = False
#     return redirect ('/')

def search(request):

    # reset the 'show_solution' boolean to false
    request.session['show_solution'] = False

    # search for algorithms matching the user input using the class method in models.py
    algorithms = Algorithm.objects.search(request)

    # put the search results into an object to be rendered in the template
    context = {
        'algorithms': algorithms,
    }

    # render the template and pass the object containing the search results
    return render(request, 'algo_app/results.html', context)

# def results(request):
#     # algorithms = Algorithm.objects.get_all()
#     algorithms = request.session['query']
#     print 'algorithms is ', algorithms
#     context = {
#         'algorithms': algorithms,
#     }
#     print 'context is ', context
#     return render(request, 'algo_app/results.html', context)

def random(request):

    # reset the 'show_solution' boolean to false
    request.session['show_solution'] = False

    # get a random algorithm using the class method in models.py
    random_algo = Algorithm.objects.get_random()

    # get the id of the random algorithm
    random_id = random_algo.id

    # redirect to the algorithm page by passing the algorithm ID in the URL
    return redirect(reverse('algorithm', kwargs={'id': random_id}))

# def manage(request):
#     tags = Tag.objects.get_all()
#     languages = Language.objects.get_all()
#     algorithms = Algorithm.objects.get_all()
#     context = {
#         'tags': tags,
#         'languages': languages,
#         'algorithms': algorithms,
#     }
#     return render(request, 'algo_app/manage.html', context)

# TAGS ########################################################################
# def create_tag(request):
#     results = Tag.objects.create_tag(request)
#     if results[0]:
#         return redirect('/manage')
#     else:
#         for each in results[1]:
#             messages.info(request, each)
#         return redirect('/manage')

# def edit_tag(request, id):
#     request.session['type'] = 'tag'
#     this_tag = Tag.objects.get_one(id)
#     context = {
#         'this_item': this_tag,
#         'this_item_value': this_tag.tag
#     }
#     return render(request, 'algo_app/edit_tl.html', context)

# def update_tag(request, id):
#     Tag.objects.update_tag(request, id)
#     return redirect('/manage')

# def destroy_tag(request, id):
#     Tag.objects.destroy_tag(request, id)
#     return redirect('/manage')

# LANGUAGES ###################################################################
# def create_language(request):
#     results = Language.objects.create_language(request)
#     if results[0]:
#         return redirect('/manage')
#     else:
#         for each in results[1]:
#             messages.info(request, each)
#         return redirect('/manage')

# def edit_language(request, id):
#     request.session['type'] = 'language'
#     this_language = Language.objects.get_one(id)
#     context = {
#         'this_item': this_language,
#         'this_item_value': this_language.language
#     }
#     return render(request, 'algo_app/edit_tl.html', context)

# def update_language(request, id):
#     Language.objects.update_language(request, id)
#     return redirect('/manage')

# def destroy_language(request, id):
#     Language.objects.destroy_language(request, id)
#     return redirect('/manage')

# SOLUTIONS ##################################################################
# def create_solution(request, id):
#     validation = Solution.objects.validate_solution(request)
#     if validation[0]:
#         results = Solution.objects.create_solution(request, id)
#     else:
#         for each in validation[1]:
#             messages.info(request, each)
#         return redirect('/manage')
#     return redirect('/')

# def edit_solution(request, id):
#     return  render(request, 'algo_app/edit.html')

# def update_solution(request, id):
#     # validation and ORM update
#     # if not validated, redirect('/algorithm/(?P<id>\d+)/edit') with error messages
#     return redirect('/')

# def delete_solution(request, id):
#     return  render(request, 'algo_app/delete.html')

# def destroy_solution(request, id):
#     Solution.objects.destroy_one_solution(request, id)
#     return redirect('/')

# ALGORITHMS ##################################################################
# def create_algorithm(request):
#     validation = Algorithm.objects.validate_algorithm(request)
#     if validation[0]:
#         results = Algorithm.objects.create_algorithm(request)
#         if 'algo_and_solution' in request.POST:
#             create_solution(request, results[1])   ###
#     else:
#         for each in validation[1]:
#             messages.info(request, each)
#         return redirect('/manage')
#     return redirect('/')

# def add_solution(request, id):
#     validation = Solution.objects.validate_solution(request)
#     if validation[0]:
#         results = Solution.objects.create_solution(request, id)
#     else:
#         for each in validation[1]:
#             messages.info(request, each)
#         return redirect('/manage')
#     return redirect('/')

def show(request, id):

    # get the algorithm and its associated information from database tables using the class methods in models.py
    this_algorithm = Algorithm.objects.show_one(request, id)
    algorithm_tags = Tag.objects.get_algorithm_tags(request, id)
    solutions = Solution.objects.get_solutions(request, id)
    languages = Language.objects.get_all()

    # put the retrieved data into an object to be passed to the template
    context = {
        'algorithm': this_algorithm,
        'algorithm_tags': algorithm_tags,
        'solutions': solutions,
        'languages': languages,
    }

    # render the template and pass the object containing the algorithm information
    return render(request, 'algo_app/algorithm.html', context)

# \/ \/ \/ REPLACED WITH JQUERY on #show_hide button #########################
# def show_solution(request, id):
#     request.session['show_solution'] = True
#     return redirect(reverse('algorithm', kwargs={'id': id}))
#
# def hide_solution(request, id):
#     request.session['show_solution'] = False
#     return redirect(reverse('algorithm', kwargs={'id': id}))
# ^ ^ ^ REPLACED WITH JQUERY on #show_hide button ############################

# def edit(request, id):
#     return  render(request, 'algo_app/edit.html')

# def update(request, id):
#     # validation and ORM update
#     # if not validated, redirect('/algorithm/(?P<id>\d+)/edit') with error messages
#     return redirect('/')

# def delete(request, id):
#     return  render(request, 'algo_app/delete.html')

# def destroy(request, id):
#     Algorithm.objects.destroy(request, id)
#     return redirect('/')
