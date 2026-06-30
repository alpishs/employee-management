import { useEffect, useState } from "react";
import api from "../services/api";

function EmployeePage() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchEmployees() {
      try {
        const response = await api.get("/employees");
        setEmployees(response.data);
      } catch (err) {
        console.error(err);
        setError("Failed to fetch employees");
      } finally {
        setLoading(false);
      }
    }

    fetchEmployees();
  }, []);

  if (loading) {
    return <h3>Loading employees...</h3>;
  }

  if (error) {
    return <h3>{error}</h3>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Employees</h2>

      {employees.length === 0 ? (
        <p>No employees found.</p>
      ) : (
        <table
          border="1"
          cellPadding="10"
          style={{ borderCollapse: "collapse", width: "100%" }}
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Role</th>
            </tr>
          </thead>

          <tbody>
            {employees.map((employee) => (
              <tr key={employee.id}>
                <td>{employee.id}</td>
                <td>{employee.name}</td>
                <td>{employee.role}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default EmployeePage;