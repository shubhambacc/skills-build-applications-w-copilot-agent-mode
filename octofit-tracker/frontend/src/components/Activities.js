import React, { useEffect, useState } from 'react';

const Activities = () => {
  const apiBase = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', apiBase);
    fetch(apiBase)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      });
  }, [apiBase]);

  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-body">
        <h2 className="card-title mb-3 text-primary">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((a, i) => (
                <tr key={i}>
                  <td>{i + 1}</td>
                  <td>{a.type}</td>
                  <td>{a.duration}</td>
                  <td>{a.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Activities;
