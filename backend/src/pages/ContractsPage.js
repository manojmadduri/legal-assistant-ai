import React, { useState } from 'react';
import axios from 'axios';

const ContractsPage = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [generatedContract, setGeneratedContract] = useState('');

  const handleGenerateContract = async () => {
    try {
      const response = await axios.post('http://localhost:8000/contracts/create', {
        title,
        content
      });
      setGeneratedContract(response.data.content);
    } catch (error) {
      console.error('Error generating contract', error);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Contracts</h1>
      <input
        type="text"
        placeholder="Contract Title"
        className="mb-4 p-2 w-full border rounded"
        value={title} onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Contract Details"
        className="mb-4 p-2 w-full border rounded"
        rows="6"
        value={content} onChange={(e) => setContent(e.target.value)}
      ></textarea>
      <button onClick={handleGenerateContract} className="bg-blue-600 text-white py-2 px-4 rounded">Generate Contract</button>

      {generatedContract && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h2 className="text-xl font-semibold mb-2">Generated Contract:</h2>
          <p>{generatedContract}</p>
        </div>
      )}
    </div>
  );
};

export default ContractsPage;
