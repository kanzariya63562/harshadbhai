import React from 'react';

const ReadList = ({ items }) => {
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>{/* Render item details */}</li>
      ))}
    </ul>
  );
};

export default ReadList;