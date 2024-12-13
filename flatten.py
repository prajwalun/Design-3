# The NestedIterator class provides an iterator for nested lists, flattening them for sequential access.

# During initialization:
# - Flatten the nested list into a single list using a helper function.
# - Store the flattened list and initialize an index for tracking the current position.

# next returns the next integer in the flattened list and increments the index.
# hasNext checks if there are more elements in the flattened list.

# TC: O(n) - Flattening the list processes all elements once.
# SC: O(n) - Space for the flattened list and recursion stack during flattening.


class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.flattenedList = []
        self.currentIndex = 0

        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    flatten(item.getList())

        flatten(self.nestedList)

    def next(self):
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number

    def hasNext(self):
        return self.currentIndex < len(self.flattenedList)
