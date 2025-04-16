// src/App.tsx
// App container with Tailwind layout
// Pseudocode:
// - Render navigation
// - Route between CheckIn, FleetDashboard, Agreement

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CheckIn from './pages/CheckIn';
import FleetDashboard from './pages/FleetDashboard';
import Agreement from './pages/Agreement';

const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow px-6 py-4 flex justify-between">
          <h1 className="text-lg font-bold text-blue-600">Loaner Platform</h1>
          <div className="space-x-4">
            <Link to="/" className="text-sm text-gray-700 hover:text-blue-600">Check-In</Link>
            <Link to="/fleet" className="text-sm text-gray-700 hover:text-blue-600">Fleet</Link>
            <Link to="/agreement" className="text-sm text-gray-700 hover:text-blue-600">Agreement</Link>
          </div>
        </nav>

        <main className="p-6">
          <Routes>
            <Route path="/" element={<CheckIn />} />
            <Route path="/fleet" element={<FleetDashboard />} />
            <Route path="/agreement" element={<Agreement />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;