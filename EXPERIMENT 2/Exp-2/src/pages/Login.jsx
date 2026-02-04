import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const { setIsAuthenticated } = useAuth();
    const navigate = useNavigate();

    const handleLogin = () => {
        setIsAuthenticated(true);
        navigate("/");
    };

    return (
        <div style={{ backgroundColor: "black", padding: "20px" }}>
            <hr />
            <h2 style={{ color: "#f8950bff" }}>Login</h2>
            <button onClick={handleLogin}
                style={{
                    background: "linear-gradient(135deg, #ff4d4d, #c1121f)",
                    color: "white",
                    border: "none",
                    padding: "12px 26px",
                    borderRadius: "30px",
                    fontSize: "15px",
                    fontWeight: "600",
                    letterSpacing: "0.5px",
                    cursor: "pointer",
                    boxShadow: "0 8px 20px rgba(193, 18, 31, 0.4)",
                    transition: "all 0.3s ease"
                }}
            >Login</button>
        </div>
    );
};

export default Login;
