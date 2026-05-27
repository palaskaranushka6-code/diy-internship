import Link from "next/link";
import { useRouter } from "next/router";

export default function Breadcrumb() {
  const router = useRouter();

  // Split current path
  const pathParts = router.pathname
    .split("/")
    .filter((part) => part);

  return (
    <div style={{ marginBottom: "20px" }}>
      <Link href="/">Home</Link>

      {pathParts.map((part, index) => {
        // Generate path link
        const href =
          "/" + pathParts.slice(0, index + 1).join("/");

        return (
          <span key={href}>
            {" / "}
            <Link href={href}>{part}</Link>
          </span>
        );
      })}
    </div>
  );
}