import { useState } from "react";

const Question = ({ question, options, answer }) => {
  const [hidden, setHidden] = useState('');
  return (
    <div className={`card w-full bg-base-100 shadow-xl my-2 ${hidden}`}>
      <div className="card-body">
        <h2 className="card-title">{question}</h2>
        {options.map((opt) => (
          <p key={`${question}-${opt}-${answer}`}>{opt}</p>
        ))}

        <div className="collapse">
          <input type="checkbox" />
          <div className="collapse-title text-xl font-medium px-0">
            Reveal Answer
          </div>
          <div className="collapse-content">
            <p>{answer}</p>
            <button className="btn btn-danger w-full my-8"
            onClick={() => {
                setHidden('hidden');
            }}
            >Hide Question</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Question;
