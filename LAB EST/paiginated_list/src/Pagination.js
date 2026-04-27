import React, { useState } from "react";
import data from "./data";

const ITEMS_PER_PAGE = 5;

function Pagination() {
  const [page, setPage] = useState(1);
  const totalPages = Math.ceil(data.length / ITEMS_PER_PAGE);
  const start = (page - 1) * ITEMS_PER_PAGE;
  const items = data.slice(start, start + ITEMS_PER_PAGE);

  return (
    <div>
      <h2>Paginated List</h2>

      {items.map((item) => (
        <p key={item.id}>{item.name}</p>
      ))}

      <button disabled={page === 1} onClick={() => setPage(page - 1)}>
        Previous
      </button>

      <span> Page {page} of {totalPages} </span>

      <button
        disabled={page === totalPages}
        onClick={() => setPage(page + 1)}
      >
        Next
      </button>
    </div>
  );
}

export default Pagination;