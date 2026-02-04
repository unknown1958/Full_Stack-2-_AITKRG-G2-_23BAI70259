import logs from "../data/logs";

const sum =()=>{
    logs.reduce((acc, log) => acc + log.carbon, 0);
}
const Logs = () => {
    return (
        <div style={{backgroundColor: "black", padding: "20px", color: "white"}}>
            <hr />
            <h2 style={{color: "#f8950bff"}}>Logs</h2>
            <ol>
                {logs.map((log) => (
                    <li key={log.id} style={{
                            color: log.carbon > 4 ? "red" : "lightgreen",
                            marginBottom: "8px"}}>
                        {log.activity}: {log.carbon} kg CO2
                    </li>

                ))}
            </ol>
            <p style={{color: "#f559f5ff"}}>Total Carbon Emission: {logs.reduce((acc, log) => acc + log.carbon, 0)} kg CO2</p>
        </div>
    )
}

export default Logs;