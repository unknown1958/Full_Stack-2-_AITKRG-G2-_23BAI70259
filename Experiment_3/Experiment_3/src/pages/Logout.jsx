import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Logout = () => {
    const { setAuthenticated } = useAuth();   
    const navigate = useNavigate(); 

    const handleLogout = () => {
        
        setAuthenticated(false);
        navigate("/login");
    };

    return (
        <div>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Logout;
