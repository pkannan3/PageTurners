// Use the API in your React components:
// Example for fetching books:

// import React, { useEffect, useState } from 'react';
// import { getBooks } from './services/api';

// const Books = () => {
//   const [books, setBooks] = useState([]);

//   useEffect(() => {
//     const fetchBooks = async () => {
//       const response = await getBooks();
//       setBooks(response.data);
//     };

//     fetchBooks();
//   }, []);

//   return (
//     <div>
//       <h1>Books</h1>
//       <ul>
//         {books.map(book => (
//           <li key={book.id}>{book.title}</li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default Books;
