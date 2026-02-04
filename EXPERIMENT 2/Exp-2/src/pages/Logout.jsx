import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Logout = () => {
    const { logout } = useAuth();   // ✅ hook inside component
    const navigate = useNavigate(); // ✅ hook inside component

    const handleLogout = () => {
        
        navigate("/login");
        logout(true);
    };

    return (
        <div style={{ backgroundColor: "black", padding: "20px" }}>
            <button
                onClick={handleLogout}
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
            >
                Logout
            </button>
        </div>
    );
};

export default Logout;
