import React, { useState } from 'react';
import axios from 'axios';

const CompliancePage = () => {
  const [document, setDocument] = useState('');
  const [complianceResult, setComplianceResult] = useState('');

  const handleCheckCompliance = async () => {
    try {
      const response = await axios.post('http://localhost:8000/compliance/check', {
        document
      });
      setComplianceResult(response.data);
    } catch (error) {
      console.error('Error checking compliance', error);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Compliance Check</h1>
      <textarea
        placeholder="Paste your document here"
        className="mb-4 p-2 w-full border rounded"
        rows="6"
        value={document} onChange={(e) => setDocument(e.target.value)}
      ></textarea>
      <button onClick={handleCheckCompliance} className="bg-blue-600 text-white py-2 px-4 rounded">Check Compliance</button>

      {complianceResult && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h2 className="text-xl font-semibold mb-2">Compliance Result:</h2>
          <pre>{JSON.stringify(complianceResult, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default CompliancePage;
