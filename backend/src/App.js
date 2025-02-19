import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import ContractsPage from './pages/ContractsPage';
import CompliancePage from './pages/CompliancePage';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/contracts" element={<ContractsPage />} />
        <Route path="/compliance" element={<CompliancePage />} />
      </Routes>
    </Router>
  );
}

export default App;
