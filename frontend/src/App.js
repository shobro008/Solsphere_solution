import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [machines, setMachines] = useState([]);

  const loadMachines = async () => {
    try {
      const response = await axios.get('http://localhost:8000/machines');
      setMachines(response.data);
    } catch (error) {
      console.error('Failed to fetch machines:', error);
    }
  };

  useEffect(() => {
    loadMachines();

    // Optional: auto-refresh every 10 seconds
    const interval = setInterval(loadMachines, 10000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Machine Status Dashboard</h1>

      {machines.length === 0 ? (
        <p>No machine data available.</p>
      ) : (
        <table border="1" cellPadding="8" style={{ borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th>Machine ID</th>
              <th>OS</th>
              <th>Encryption</th>
              <th>Antivirus</th>
              <th>OS Update</th>
              <th>Sleep Timeout</th>
              <th>Last Updated</th>
            </tr>
          </thead>
          <tbody>
            {machines.map((m) => (
              <tr key={m.machine_id}>
                <td>{m.machine_id}</td>
                <td>{m.os}</td>
                <td>{m.encryption}</td>
                <td>{m.antivirus}</td>
                <td>{m.os_update}</td>
                <td>{m.sleep_timeout}</td>
                <td>{new Date(m.last_updated).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
