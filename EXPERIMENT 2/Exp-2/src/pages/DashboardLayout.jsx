import { Link, Outlet } from "react-router-dom";
import Logout from "./Logout";

const DashboardLayout = () => {
    return (
        <div style={{backgroundColor: "black", padding: "20px"}}>
             <hr />
            <h2 style={{color: "#f8950bff"}}>Dashboard</h2>

            <nav>
                <Link style={{paddingRight: "10px", color: "#00fff0"}} to = "settings">Settings</Link>
                <Link style={{padding: "10px", color: "#00fff0"}}to = "summary">Summmary</Link>
                <Link style={{padding: "10px", color: "#00fff0"}} to = "analytics">Analytics</Link>            
            </nav>

            

            <Outlet />
            <Logout />
        </div>

    )
}

export default DashboardLayout;