import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // adjust this if your backend is running on a different port
});

export const getBooks = () => api.get('/books/');
export const createBook = (data) => api.post('/books/', data);
export const deleteBook = (id) => api.delete(`/books/${id}`);
