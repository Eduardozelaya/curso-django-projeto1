from django.test import Client, TestCase
from django.urls import reverse
from recipes.models import Recipe
from django.contrib.auth.models import User

class TestListarReceitasView(TestCase):
    def setUp(self):
        # Criar usuários
        self.users = []
        for i in range(10):
            user = User.objects.create_user(
                username=f'adão{i}',
                email=f'adão{i}@example.com',
                password='password123'
            )
            self.users.append(user)

        # Criar receitas associadas aos usuários criados
        for i in range(10):
            Recipe.objects.create(
                title=f'title-recipes-test-{i}',
                slug=f'title-recipes-test-{i}',
                author=self.users[i],
                preparation_time=30,
                servings=4
            )


    def test_pagination_renders_correct_amount_of_recipes_per_page(self):
        client = Client()
        response = client.get(reverse('recipes:search'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

        recipes = response.context['recipes']
        objects_per_page = len(recipes)

        self.assertEqual(objects_per_page, 9)

        # Verifica se os títulos das receitas estão presentes na página
        for i in range(9):
            self.assertIn(f'title-recipes-test-{i}', response.content.decode())
