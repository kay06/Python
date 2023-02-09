tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

#merged tags
merged_tags = tags_one | tags_two

print(merged_tags)


#how to remove a element from a set from another set
exclusive_to_tag_one = tags_one - tags_two

print(exclusive_to_tag_one)


exclusive_to_tag_two = tags_two - tags_one

print(exclusive_to_tag_two)

#how to only get the commen elements in 2 sets
universal_tags = tags_one & tags_two

print(universal_tags)