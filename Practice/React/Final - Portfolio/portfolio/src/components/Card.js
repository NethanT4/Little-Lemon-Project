import { Heading, HStack, Image, Text, VStack } from "@chakra-ui/react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight } from "@fortawesome/free-solid-svg-icons";
import React from "react";

const Card = ({ title, description, imageSrc }) => {
  return (
    <VStack
      spacing={0}
      borderRadius="md"
      overflow="hidden"
      bg="white"
      align="stretch"
    >
      <Image src={imageSrc} alt={title} />
      <VStack align="start" p="4" spacing="2" color="black">
        <Heading as="h3" size="md">
          {title}
        </Heading>

        <Text>{description}</Text>

        <HStack spacing={2}>
          <Text>See more</Text>
          <FontAwesomeIcon icon={faArrowRight} size="1x" />
        </HStack>
      </VStack>
    </VStack>
  )
};

export default Card;
