from django.urls import reverse
from rest_framework import test, status

from store.models import Book
from store.serializers import BooksSerializer


class BooksAPITestCase(test.APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=25)
        book_2 = Book.objects.create(name='Test book 2', price=55)
        url = reverse('book-list')
        # url = reverse('book-detail')
        response = self.client.get(url)
        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        # serializer_data = BooksSerializer(book_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
