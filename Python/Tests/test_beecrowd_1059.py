from Python.Problems import beecrowd_1059


# check zero_to_hundred of exercise 1059
def test_beginner1059_zero_to_hundred_one() -> None:
    result = beecrowd_1059.zero_to_hundred()
    assert (
        result
        == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n22\n24\n26\n28\n30\n32\n34\n36\n38\n40\n42\n44\n46\n48\n50\n52\n54\n56\n58\n60\n62\n64\n66\n68\n70\n72\n74\n76\n78\n80\n82\n84\n86\n88\n90\n92\n94\n96\n98\n100"
    )
