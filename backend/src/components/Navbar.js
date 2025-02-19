import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <div className="flex justify-between items-center">
        <Link to="/" className="text-white text-xl font-bold">Legal Assistant</Link>
        <div>
          <Link to="/dashboard" className="text-white px-4">Dashboard</Link>
          <Link to="/contracts" className="text-white px-4">Contracts</Link>
          <Link to="/compliance" className="text-white px-4">Compliance</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
