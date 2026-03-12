import logs from "./data.js";

const highcarbon = logs.filter((log) => {
  if (log.carbon >= 4) {
    return true;
  } else {
    return false;
  }
});

const lowcarbon = logs.filter((log) => {
  if (log.carbon <= 3) {
    return true;
  } else {
    return false;
  }
});


function Logs() {
  return (
    <>
      <h3>Activities having carbon footprint greater than equal to 4 : </h3>
      <ul style={{color : "red"}}>
        {highcarbon.map((log) => (
          <li key = {log.id}>
            {log.activity} — {log.carbon}
          </li>
        ))}
      </ul>
      <br />
      <br />
      <h3>Activities having carbon footprint less than equal to 3 : </h3>
      <ul style = {{color : "green"}}>
        {lowcarbon.map((log) => (
          <li key = {log.id}>
            {log.activity} — {log.carbon}
          </li>
        ))}
      </ul>
    </>
  );
}

export default Logs;
