import { departmentsAccessToQuery } from "@/src/graphql/queries/deptAccess";
import { useQuery } from "@apollo/client";
import DepartmentCard from "components/DepartmentCard";
import { useRouter } from "next/router";

export default function Degree() {
  const router = useRouter();
  const { regulation, programme, degree, semester } = router.query;

  const { data, loading, error } = useQuery(departmentsAccessToQuery, {
    ssr: false,
  });

  if (loading) return "Loading...";
  if (error) return <p>Error: {error.message}</p>;
  const programme_data = data?.departmentsAccessTo;

  const filteredData = programme_data.filter(function (item, n) {
    return (
      item["course"]["regulation"]["year"] == regulation &&
      item["course"]["department"]["programme"]["name"] == programme &&
      item["course"]["department"]["degree"]["name"] == degree &&
      item["course"]["semester"] == semester
    );
  });

  console.log(filteredData);
  return (
    <>
      <DepartmentCard data={filteredData} currentPath={router.asPath} />
    </>
  );
}
// <BranchCard data={filteredData} currentPath={router.asPath} />
