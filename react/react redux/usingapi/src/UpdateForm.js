import React, { useState } from 'react';

const UpdateForm = ({ item, onUpdate }) => {
  const [formData, setFormData] = useState({
    // Initialize form fields with item data
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdate(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Render form fields pre-filled with item data */}
      <button type="submit">Update</button>
    </form>
  );
};

export default UpdateForm;