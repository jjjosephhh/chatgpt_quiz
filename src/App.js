import Navbar from "./components/Navbar";
import Layout from "./components/Layout";
import QuestionList from "./components/QuestionList";

function App() {
  return (
    <>
      <Navbar />
      <Layout>
        <QuestionList />
      </Layout>
    </>
  );
}

export default App;
