import Layout from "./Layout";
import questions from "../questions/questions.json";
import Question from "./Question";
import _ from "lodash";

const QuestionList = () => {
  return (
    <Layout>
      {_.shuffle(questions).map((q) => (
        <Question key={`${q.question}-${q.answer}`} {...q} />
      ))}
    </Layout>
  );
};

export default QuestionList;
