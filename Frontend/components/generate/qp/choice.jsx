const Choice = ({ part, count, mark, subdivsel, optsel, store, isAnswer }) => {
  return (
    <table className="w-full">
      <tbody>
        {part == "A" && !isAnswer && (
          <tr>
            <td
              className="text-center break-inside-avoid"
              colSpan={subdivsel + optsel + 6}
            >
              <div className="font-bold">REVISED BLOOMS TAXONOMY(RBT)</div>
              <div>
                L1-Remembering, L2-Understanding, L3-Applying, L4-Analyzing,
                L5-Evaluating, L6-Creating
              </div>
            </td>
          </tr>
        )}
        <tr>
          <td
            className="text-center font-bold"
            colSpan={subdivsel + optsel + 2}
          >
            Part-{part}-({count}x{mark}={count * mark} marks)
            <br />
            {count > 1 && !isAnswer && "(Answer all the questions)"}
          </td>
          {!isAnswer && (
            <>
              <td className="text-center font-bold px-2">CO</td>
              <td className="text-center font-bold px-2">
                BT
                <br />
                Level
              </td>
              <td className="text-center font-bold px-2">
                Univ
                <br />
                QP
              </td>
              <td className="text-center font-bold px-2">
                Mark
                <br />
                Allocated
              </td>
            </>
          )}
        </tr>
      </tbody>
      <tbody>{store}</tbody>
    </table>
  );
};

export default Choice;
