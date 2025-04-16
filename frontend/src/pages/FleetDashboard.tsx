// pages/FleetDashboard.tsx
// Admin view for active vehicles and agreements

import React from 'react';

const mockFleet = [
  { unit: 'P7N04476', model: 'BMW 330i', status: 'Out', customer: 'Megan Harper', ro: '282504' },
  { unit: 'PCN69371', model: 'BMW X3', status: 'Available', customer: '', ro: '' },
  { unit: 'R9U10991', model: 'BMW 530e', status: 'Out', customer: 'Joseph Miles', ro: '282532' },
];

const FleetDashboard: React.FC = () => {
  return (
    <div className="max-w-5xl mx-auto py-8">
      <h1 className="text-2xl font-semibold text-gray-800 mb-6">Fleet Dashboard</h1>

      <table className="min-w-full bg-white border rounded shadow overflow-hidden">
        <thead className="bg-gray-100">
          <tr>
            <th className="text-left px-4 py-2 text-sm font-medium text-gray-600">Unit #</th>
            <th className="text-left px-4 py-2 text-sm font-medium text-gray-600">Model</th>
            <th className="text-left px-4 py-2 text-sm font-medium text-gray-600">Status</th>
            <th className="text-left px-4 py-2 text-sm font-medium text-gray-600">Customer</th>
            <th className="text-left px-4 py-2 text-sm font-medium text-gray-600">RO #</th>
          </tr>
        </thead>
        <tbody>
          {mockFleet.map((car, idx) => (
            <tr key={idx} className="border-t hover:bg-blue-50">
              <td className="px-4 py-2 font-mono text-blue-700">{car.unit}</td>
              <td className="px-4 py-2">{car.model}</td>
              <td className="px-4 py-2 text-sm text-gray-700">{car.status}</td>
              <td className="px-4 py-2">{car.customer || '-'}</td>
              <td className="px-4 py-2">{car.ro || '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FleetDashboard;