import React, { useEffect, useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  SafeAreaView,
  ScrollView,
  FlatList,
  TextInput,
} from "react-native";
import emojiss from "./src/emoji.json";

export default function App() {
  const [searchfield, setSearchfield] = useState("");

  const [emojis, setEmojis] = useState(emojiss["스마일리 & 감정"]);

  useEffect(() => {
    const filteredEmojis = emojiss["스마일리 & 감정"].filter((emoji) => {
      return emoji.name.toString().includes(searchfield);
    });
    setEmojis(filteredEmojis);
    console.log(searchfield.toString());
    console.log(emojis);
  }, [searchfield]);

  const Item = ({ emoji }) => (
    <TouchableOpacity>
      <View style={styles.item}>
        <Text style={styles.emoji}>{emoji}</Text>
      </View>
    </TouchableOpacity>
  );

  const renderItem = ({ item }) => <Item emoji={item.emoji} />;

  return (
    <SafeAreaView
      style={{ flex: 1, justifyContent: "center", alignItems: "center" }}
    >
      <View>
        <TextInput
          placeholder="이모지를 검색하세요"
          onChangeText={(text) => {
            setSearchfield(text);
          }}
        ></TextInput>
      </View>
      <FlatList
        numColumns={8}
        data={emojis}
        renderItem={renderItem}
        keyExtractor={(item) => item.emoji}
      ></FlatList>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  item: {
    width: 45,
    height: 45,
  },
  emoji: {
    fontSize: 38,
  },
});
