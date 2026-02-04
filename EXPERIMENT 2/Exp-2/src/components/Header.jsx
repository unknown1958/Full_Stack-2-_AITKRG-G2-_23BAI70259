import { Link } from "react-router-dom";

const Header = () => {
    return (
        <header style = {{
            padding: '10px',
            backgroundColor: "#000000ff",
            color : 'white',
            textAlign: 'center',
        }}> 
            <h1>EcoTrack-2</h1>
            <Link style={{paddingRight: "10px", color: "#00fff0"}} to = "/">Dashboard</Link>
            <Link style={{padding: "10px", color: "#00fff0"}} to = "/logs">Logs</Link>
            <Link style={{padding: "10px", color: "#00fff0"}} to = "/login">Login</Link>
        </header>
    )
}
export default Header;